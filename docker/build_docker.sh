#!/usr/bin/env bash
<<EOF

   Blog Tool \ Build All Architectures

   Build the Docker container images to support all architectures.

EOF
CURRENT_SCRIPT_DIRECTORY=${CURRENT_SCRIPT_DIRECTORY:-$(dirname $(realpath ${BASH_SOURCE[0]:-${(%):-%x}}))}
export SHARED_EXT_SCRIPTS_PATH=${SHARED_EXT_SCRIPTS_PATH:-$(realpath $CURRENT_SCRIPT_DIRECTORY/../scripts)}
export CURRENT_SCRIPT_FILENAME=${CURRENT_SCRIPT_FILENAME:-$(basename ${BASH_SOURCE[0]:-${(%):-%x}})}
export CURRENT_SCRIPT_FILENAME_BASE=${CURRENT_SCRIPT_FILENAME%.*}
. "$SHARED_EXT_SCRIPTS_PATH/shared_functions.sh"
write_header

if ! is_docker_installed; then
    write_error "build_all_arch" "Failed: Docker is not installed on this system"
    exit 1
fi

if ! is_command_available yq; then
    write_error "build_all_arch" "Failed: Unable to find the command \"yq\""
    exit 1
fi

# File to analyze (default: docker-compose.yml)
export DOCKER_PROJECT_PATH=$CURRENT_SCRIPT_DIRECTORY
export DOCKER_PROJECT_COMPOSE_FILEPATH="$DOCKER_PROJECT_PATH/docker-compose.yaml"
export DOCKER_PROJECT_CONTAINERS_PATH=$DOCKER_PROJECT_PATH/containers
export CONTAINERS_ROOT=$DOCKER_PROJECT_PATH/containers

if [ ! -e "$DOCKER_PROJECT_COMPOSE_FILEPATH" ]; then
    write_error "build_all_arch" "Failed: Unable to find the docker-compose project file \"$DOCKER_PROJECT_COMPOSE_FILEPATH\""
    exit 1
fi

# Extract services that have 'build' defined
# write_info "build_all_arch" "Services:"
BUILD_IMAGES=$(yq '.services | to_entries | map(select(.value.build? != null)) | .[].key' "$DOCKER_PROJECT_COMPOSE_FILEPATH")

if [ ! ${#BUILD_IMAGES[@]} -gt 0 ]; then
    write_error "build_all_arch" "No container images to build."
    write_error "build_all_arch" "Project File: \"$DOCKER_PROJECT_COMPOSE_FILEPATH\""
    exit 1
fi

write_info "build_all_arch" "Building:"
for build_image in ${BUILD_IMAGES[@]}; do
    write_info "build_all_arch" "↪ $build_image"
done

# Set the image name and version/tag
# IMAGE_NAME="your_image_name"
VERSION="latest"

# Specify the architectures to build for
ARCHS=("linux/amd64" "linux/arm64" "linux/arm/v7")
VERSIONS=("development" "production")

export DOCKER_BUILDKIT=1

# # Create a builder instance if not already available
# docker buildx inspect mybuilder > /dev/null 2>&1
# if [ $? -ne 0 ]; then
#     docker buildx create --name mybuilder --use
# fi
pushd "$DOCKER_PROJECT_PATH" 2>&1 >/dev/null

# Build images for each architecture and push them individually
for service in ${BUILD_IMAGES[@]}; do
    write_info "build_all_arch" "*********************************"
    write_info "build_all_arch" "Building Service: \"$service\""
    write_info "build_all_arch" "*********************************"
    write_info "build_all_arch" "↪ Service: $service"
    SERVICE_BUMPVERSION_FILE_PATH=$DOCKER_PROJECT_CONTAINERS_PATH/$service/build/.bumpversion.toml
    SERVICE_VERSION=$(yq e '.tool."bumpversion".current_version' $SERVICE_BUMPVERSION_FILE_PATH)
    write_info "build_all_arch" "↪ Service Version: $SERVICE_VERSION"
    SERVICE_DOCKERFILE_PATH=$(yq ".services[\"$service\"][\"build\"][\"dockerfile\"]" $DOCKER_PROJECT_COMPOSE_FILEPATH)
    if [ -z "$SERVICE_DOCKERFILE_PATH" ]; then
        write_error "build_all_arch" "The Dockerfile for \"$service\" could not be resolved."
        continue
    fi
    SERVICE_DOCKERFILE_PATH_ABS=$(echo $SERVICE_DOCKERFILE_PATH | envsubst)
    write_info "build_all_arch" "↪ Dockerfile: $SERVICE_DOCKERFILE_PATH_ABS"
    for version in ${VERSIONS[@]}; do
        TAG="${service}:${version}"
        write_info "build_all_arch" "↪ Version: $version"
        for ARCH in "${ARCHS[@]}"; do
            TAG_ARCH="${TAG}-${ARCH//\//-}"

            # TAG="${service}:${VERSION}-${ARCH//\//-}"
            # write_info "build_all_arch" "Building Container Image ($DOCKER_PROJECT_COMPOSE_FILEPATH)"
            write_info "build_all_arch" "↪ Architecture: $ARCH"
            # docker buildx build --platform ${ARCH} -t ${TAG_ARCH} \
            BUILDKIT_PROGRESS=plain docker compose -f $DOCKER_PROJECT_COMPOSE_FILEPATH build \
            --build-arg BUILD_DATE="$(date -u +'%Y-%m-%dT%H:%M:%SZ')" \
            --build-arg BUILD_VERSION="${version}" \
            --build-arg BUILD_UID="$(uuidgen)" "$service"
            # --progress=plain $(dirname "$SERVICE_DOCKERFILE_PATH_ABS")
            # --parallel "$SERVICE_DOCKERFILE_PATH"
            # --parallel .
            #> /dev/null 2>&1

            # docker buildx build --platform ${ARCH} -t ${TAG_ARCH} --push .
            # docker buildx build --platform ${ARCH} -t ${TAG_ARCH} .
            # if ! write_response "build_all_arch" "Build: $service $ARCH $TAG"; then
            #     write_error "build_all_arch" "Failed: Unable to build container image"
            #     write_error "build_all_arch" "↪ Service: $service"
            #     write_error "build_all_arch" "↪ Architecture: $ARCH"
            #     write_error "build_all_arch" "↪ Tag: $TAG"
            # fi
        done
    done
done

popd 2>&1 >/dev/null

# Create and push a manifest to combine all architectures
# write_info "build_all_arch" "Creating and pushing manifest..."
# docker manifest create ${IMAGE_NAME}:${VERSION} $(for ARCH in "${ARCHS[@]}"; do echo "${IMAGE_NAME}:${VERSION}-${ARCH//\//-}"; done)

# # Annotate the manifest with specific architecture information
# for ARCH in "${ARCHS[@]}"; do
#     docker manifest annotate ${IMAGE_NAME}:${VERSION} ${IMAGE_NAME}:${VERSION}-${ARCH//\//-} --os linux --arch ${ARCH#*/}
# done

# # Push the manifest
# docker manifest push ${IMAGE_NAME}:${VERSION}

# write_info "build_all_arch" "Multi-architecture Docker image created and pushed: ${IMAGE_NAME}:${VERSION}"
# write_success "build_all_arch" "Done"
exit 0
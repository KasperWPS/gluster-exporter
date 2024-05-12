#!/bin/bash

set -e

export GOPATH=~/go
export PATH=${PATH}:${GOPATH}/bin

mkdir -p ${GOPATH}/{bin,pkg,src}

sudo dnf install golang rpmdevtools -y

rpmdev-setuptree

cd gluster-exporter
# Download project dependencies
go mod tidy

git archive --format=tar.gz --prefix=gluster-exporter-1.0/ -o gluster-exporter-1.0.tar.gz HEAD

mv gluster-exporter-1.0.tar.gz ~/rpmbuild/SOURCES

cd ..

rpmbuild -ba gluster-exporter.spec
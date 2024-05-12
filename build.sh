#!/bin/bash

set -e

rpmdev-setuptree

cd gluster-exporter
git archive --format=tar.gz --prefix=gluster-exporter-1.0/ -o gluster-exporter-1.0.tar.gz HEAD

mv gluster-exporter-1.0.tar.gz ~/rpmbuild/SOURCES

cd ..

rpmbuild -ba gluster-exporter.spec
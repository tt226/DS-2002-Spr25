#!/bin/bash

FILENAME=$1
BUCKET=$2
EXPIRES=$3


if [ ! -f "$FILENAME" ]; then
  echo "File not found: $FILENAME"
  exit 1
fi

aws s3 cp "$FILENAME" s3://$BUCKET/
aws s3 presign --expires-in "$EXPIRES" s3://$BUCKET/$FILENAME
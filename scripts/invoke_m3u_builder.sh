#! /usr/bin/env bash

REGION=$1
POLLY_ASSETS_BUCKET=$2
STACK_NAME=$3

M3U_FUNCTION_NAME=$(aws cloudformation --region ${REGION} describe-stacks --stack $STACK_NAME --output text | grep OUTPUTS | grep m3uBuilderFunctionName | cut -f4)

aws lambda invoke --function-name ${M3U_FUNCTION_NAME} --cli-binary-format raw-in-base64-out\
  --payload "{\"s3Bucket\": \"${POLLY_ASSETS_BUCKET}\", \"m3uFile\": \"polly-faq-reader/mp3/23_oct_65_ss.m3u\"}" \
  --region ${REGION} \
  m3u_out.txt

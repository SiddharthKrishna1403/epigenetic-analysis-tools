#!/bin/bash

TOOL=$1
shift

case $TOOL in
    "fastqc")
        docker-compose run --rm biotools fastqc "$@"
        ;;
    "trimmomatic")
        docker-compose run --rm biotools trimmomatic "$@"
        ;;
    "hisat2")
        docker-compose run --rm biotools hisat2 "$@"
        ;;
    "stringtie")
        docker-compose run --rm biotools stringtie "$@"
        ;;
    "hic-pro")
        docker-compose run --rm biotools HiC-Pro "$@"
        ;;
    "juicer")
        docker-compose run --rm biotools juicer "$@"
        ;;
    "deseq2")
        docker-compose run --rm biotools R "$@"
        ;;
    "jupyter")
        docker-compose --profile jupyter up
        ;;
    *)
        echo "Unknown tool: $TOOL"
        echo "Available tools: fastqc, trimmomatic, hisat2, stringtie, hic-pro, juicer, deseq2, jupyter"
        exit 1
        ;;
esac

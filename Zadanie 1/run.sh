#!/bin/bash

gen_image="generator_image"
reporter_image="reporter_image"

case "$1" in
    build_generator)
        docker build -t $gen_image .
        ;;

    run_generator)
        mkdir -p data
        docker run --rm -v "$(pwd)/data:/data" $gen_image
        ;;

    create_local_data)
        mkdir -p local_data
        python3 generate.py "$(pwd)/local_data"
        ;;

    build_reporter)
        docker build -f Dockerfile_report -t $reporter_image .
        ;;

    run_reporter)
        mkdir -p data
        docker run --rm -v "$(pwd)/data:/data" $reporter_image
        ;;

    structure)
        ls -R
        ;;

    clear_data)
        rm -f data/*.csv data/*.html
        ;;

    inside_generator)
        docker run --rm -v "$(pwd)/data:/data" $gen_image ls -la /data
        ;;

    inside_reporter)
        docker run --rm -v "$(pwd)/data:/data" $reporter_image ls -la /data
        ;;

    *)
        echo "Ошибка: Вы ввели неверную команду."
        echo "Использование: ./run.sh {build_generator|run_generator|create_local_data|build_reporter|run_reporter|structure|clear_data|inside_generator|inside_reporter}"
        exit 1
        ;;
esac
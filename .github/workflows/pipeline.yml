# Nome do Workflow
name: DevOpsLab Pipeline

# Evento que irá acionar a pipeline
on:
  push:
    branches:
      - main

jobs:
  Build:
    runs-on: ubuntu-latest
    steps:
      - name: Download do Repositório
        uses: actions/checkout@v4       # https://github.com/actions/checkout

      - name: Setup Python
        uses: actions/setup-python@v5   # https://github.com/actions/setup-python
        with:
          python-version: '3.10'

      - name: Install Requirements
        run:  pip install flask

      - name: Unit Test
        run: python -m unittest -v test

      - name: Login no Artifact Registry
        uses: docker/login-action@v3      # https://github.com/marketplace/actions/docker-login#google-artifact-registry-gar
        with:
          registry: '${{ vars.GOOGLE_ARTIFACT }}'
          username: _json_key
          password: '${{ secrets.GOOGLE_CREDENTIALS }}'

      - name: Build Image
        run: |
          docker build -t ${{ vars.GOOGLE_ARTIFACT }}/${{ vars.GOOGLE_PROJECT_ID }}/${{ vars.GOOGLE_REPONAME }}/${{ vars.GOOGLE_MYAPP }}:latest .

      - name: Push Image
        run: |
          docker push ${{ vars.GOOGLE_ARTIFACT }}/${{ vars.GOOGLE_PROJECT_ID }}/${{ vars.GOOGLE_REPONAME }}/${{ vars.GOOGLE_MYAPP }}:latest
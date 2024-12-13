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

  Deploy:
    needs: Build
    runs-on: ubuntu-latest

    steps:
      - name: Download do Repositório
        uses: actions/checkout@v4       # https://github.com/actions/checkout

      - name: Login no GCP
        uses: 'google-github-actions/auth@v2' # https://github.com/google-github-actions/auth
        with:
          credentials_json: '${{ secrets.GOOGLE_CREDENTIALS }}'

      - name: Cloud Run Deploy
        id: deploy
        uses: 'google-github-actions/deploy-cloudrun@v2'  # https://github.com/marketplace/actions/deploy-to-cloud-run
        with:
          service: ${{ vars.GOOGLE_MYAPP }}
          region: ${{ vars.GOOGLE_REGION }}
          image:   ${{ vars.GOOGLE_ARTIFACT }}/${{ vars.GOOGLE_PROJECT_ID }}/${{ vars.GOOGLE_REPONAME }}/${{ vars.GOOGLE_MYAPP }}:latest
          flags: '--allow-unauthenticated'

      - name: Validando a API
        run: 'curl "${{ steps.deploy.outputs.url }}"'
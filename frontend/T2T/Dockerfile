
FROM node:20-bullseye-slim as build-step

RUN mkdir -p /app

WORKDIR /frontend

COPY package.json /frontend

RUN npm install

COPY . /frontend

EXPOSE 4200

RUN npm run start
 
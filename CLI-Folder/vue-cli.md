# Vue CLI Cheat Sheet

Prerequisites: [Node.js](https://nodejs.org/en/) (>=6.x, 8.x preferred), npm version 3+ and [Git](https://git-scm.com/).

## Installation

`$ npm install -g vue-cli`

`$ yarn global add vue-cli`

## Usage

`$ vue init <template-name> <project-name>`

Example:

`$ vue init webpack my-project`

### Official Templates

Current available templates include:

[webpack](https://github.com/vuejs-templates/webpack) - A full-featured Webpack + vue-loader setup with hot reload, linting, testing & css extraction.

[webpack-simple](https://github.com/vuejs-templates/webpack-simple) - A simple Webpack + vue-loader setup for quick prototyping.

[browserify](https://github.com/vuejs-templates/browserify) - A full-featured Browserify + vueify setup with hot-reload, linting & unit testing.

[browserify-simple](https://github.com/vuejs-templates/browserify-simple) - A simple Browserify + vueify setup for quick prototyping.

[pwa](https://github.com/vuejs-templates/pwa) - PWA template for vue-cli based on the webpack template

[simple](https://github.com/vuejs-templates/simple) - The simplest possible Vue setup in a single HTML file

## Start development

To get started:

`cd <dest-dir-name>`

`npm install`

`npm run dev`

## Build

Creating a build: Artifacts will be stored in the `dist/` directory.

`npm run build`

`npm run build --prod`

Build component without manually create a Vue instance for it:

`vue build <Component.vue>`

Watch mode (as development mode but does not add hot-reloading support):

`vue build index.js --watch`

Need help:

`vue build -h`

## Test

Running unit tests

`npm run test`

Running end-to-end tests

`npm run e2e`

## Linting code

`npm run lint`

## Help

`vue help`

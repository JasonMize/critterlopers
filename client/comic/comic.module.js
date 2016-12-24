import angular from 'angular';

import comicPageComponent from './comic-page.component';

const ComicModule = angular.module('comics', [
])
    .component('comicPage', comicPageComponent);

export default ComicModule;

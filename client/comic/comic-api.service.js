
function comicAPIService($resource) {
    const api = {
        getComic(id) {
            return this.comic.get({ id }).$promise.then((data) => {
                return data;
            });
        },

        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
        ),
        comic: $resource('/api/comic/:id',
            { id: '@id' },
        ),
        cast: $resource('/api/cast/:id',
            { id: '@id' },
        ),
        issue: $resource('/api/issue/:id',
            { id: '@id' },
        ),
    };

    return api;
}

export default comicAPIService;

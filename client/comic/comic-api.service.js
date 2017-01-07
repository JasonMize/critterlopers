
function comicAPIService($resource) {
    const api = {
        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
        ),
        comic: $resource('/api/comic/:id',
            { id: '@id' },
        ),
        cast: $resource('/api/cast/:id',
            { id: '@id' },
        ),
    };

    return api;
}

export default comicAPIService;

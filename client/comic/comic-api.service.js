
function comicAPIService($resource) {
    const api = {
        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
            {
                update: {
                    method: 'PUT',
                },
            }
        ),
    };

    return api;
}

export default comicAPIService;


function comicAPIService($resource) {
    const api = {
        getComic(pageNumber) {
            return this.issuePage.get({pageNumber}).$promise.then((data) => {
                console.log('COMIC API DATA: ', data);
                return data;
            });
        },
        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
        ),
        comic: $resource('/api/comic/:pageNumber/',
            { page_number: '@pageNumber' },
        ),
        issuePage: $resource('/api/comic/:pageNumber/',
            {
                page_number: '@pageNumber'
            }
        ),
        // cast: $resource('/api/cast/:id/',
            // { id: '@id' },
        // ),
    };

    return api;
}

export default comicAPIService;

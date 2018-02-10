
function comicAPIService($resource) {
    const api = {
        // getIssue(id) {
            // return this.issue.get({ id }).$promise.then((data) => {
                // return data;
            // });
        // },
        getComic(pageNumber, navigation = '') {
            return this.issuePage.get({ pageNumber, navigation }).$promise.then((data) => {
                console.log('COMIC API DATA: ', data);
                return data;
            });
        },

        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
        ),
        comic: $resource('/api/comic/:pageNumber',
            { page_number: '@pageNumber' },
        ),
        issuePage: $resource('/api/comic/:pageNumber/:navigation',
            {
                // issueId: '@issueId',
                page_number: '@pageNumber',
                navigation: '@navigation',
            }
        ),
        // cast: $resource('/api/cast/:id',
            // { id: '@id' },
        // ),
        // issue: $resource('/api/issue/:id',
            // { id: '@id' },
        // ),
    };

    return api;
}

export default comicAPIService;

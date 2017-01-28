
function comicAPIService($resource) {
    const api = {
        getIssue(id) {
            return this.issue.get({ id }).$promise.then((data) => {
                return data;
            });
        },
        getComic(issueId, pageNumber) {
            return this.issuePage.get({ issueId, pageNumber }).$promise.then((data) => {
                return data;
            });
        },

        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
        ),
        comic: $resource('/api/comic/:id',
            { id: '@id' },
        ),
        issuePage: $resource('/api/issuepage/:issueId/:pageNumber',
            {
                issueId: '@issueId',
                pageNumber: '@pageNumber',
            }
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

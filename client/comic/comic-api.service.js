
function comicAPIService($resource) {
    const api = {
        getIssue(id) {
            return this.issue.get({ id }).$promise.then((data) => {
                return data;
            });
        },
        getComic(issueId, pageNumber, navigation = '') {
            return this.issuePage.get({ issueId, pageNumber, navigation }).$promise.then((data) => {
                // console.log('COMIC API DATA: ', data);
                return data;
            });
        },

        headerimage: $resource('/api/headerimage/:id/',
            { id: '@id' },
        ),
        comic: $resource('/api/comic/:id',
            { id: '@id' },
        ),
        issuePage: $resource('/api/issue/:issueId/comic/:pageNumber/:navigation',
            {
                issueId: '@issueId',
                pageNumber: '@pageNumber',
                navigation: '@navigation',
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

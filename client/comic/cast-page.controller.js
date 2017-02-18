
function CastPageController(comicAPIService) {
    const ctrl = this;

    function getAllCastMembers() {
        return comicAPIService.cast.get().$promise.then((data) => {
            ctrl.cast_members = data.results;
            console.log('CAST MEMBERS: ', ctrl.cast_members);
        }, (error) => {
            console.log('ERROR: ', error);
        });
    }

    function init() {
        getAllCastMembers();
    }

    console.log('HERE');
    init();
}

export default CastPageController;


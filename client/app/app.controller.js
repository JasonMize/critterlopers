
function AppController(comicAPIService) {
    const ctrl = this;

    // get a random HeaderImage
    function randomHeaderImage() {
        ctrl.maxRange = Math.floor(ctrl.headerImageList.length);
        ctrl.headerImageIndex = Math.floor(Math.random() * (ctrl.maxRange));
        ctrl.randomHeaderImage = ctrl.headerImageList[ctrl.headerImageIndex];
    }
    // get all HeaderImages
    function getHeaderImage() {
        return comicAPIService.headerimage.query().$promise.then((data) => {
            ctrl.headerImageList = data;

            randomHeaderImage();

        }).catch(function(error) {
            console.log('APP CONTROLLER: GET HEADER IMAGE: ERROR: ', error);
        });
    }

    function init() {
        getHeaderImage();
    }
    init();
}

export default AppController;


function ArchivePageController(comicAPIService) {
    console.log('ARCHIVE PAGE CONTROLLER: ', comicAPIService);
    const archCtrl = this;

    function getAllComics() {
        console.log('GET ALL COMICS CALLED');
        return comicAPIService.comic.query().$promise.then((data) => {
            archCtrl.comics = data;
            console.log('ALL COMICS ARCHIVE: ', archCtrl.comics);
        }, (error) => {
            console.log('ARCHIVE PAGE CONTROLLER: GET ALL COMICS: ERROR: ', error);
        });
    }

    function init() {
        getAllComics();
    }

    init();
}

export default ArchivePageController;


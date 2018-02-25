function AboutPageController() {
    const ctrl = this;
    ga('send', {
    hitType: 'event',
    eventCategory: 'pageview',
    eventAction: 'about',
});

}

export default AboutPageController;

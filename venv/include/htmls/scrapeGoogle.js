var casper = require("casper").create({
    verbose: false,
    logLevel: 'debug',
    pageSettings : {
        loadImages: false,
        loadPlugins: false,
        userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
});

var serchTerm = 'mars';
var url='https://google.com/';
var links = [];
var titles = [];
var arrJSON = [];
var fs =require('fs');

function getLinks() {
    var link = document.querySelectorAll('h3.r a');
    return Array.prototype.map.call(link, function(e) {
        return e.getAttribute('href');
    });
}

function getTitles() {
    var links = document.querySelectorAll('h3.r a');
    return Array.prototype.map.call(links, function(e) {
        return e.innerHTML;
    });
}

function createJSON() {
    for (index=0; index<links.length;index++) {
        arrJSON.push({
            title: titles[index],
            link: links[index]
        });
    }
    return JSON.stringify(arrJSON);
}

casper.start(url, function() {
    this.echo()
})
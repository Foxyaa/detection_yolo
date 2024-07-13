// pull down jquery into the JavaScript console
/*var images = document.getElementsByTagName('img');
var imageUrls = [];
for (var i = 0; i < images.length; i++) {
    imageUrls.push(images[i].src);
}
console.log(imageUrls);

*/
var script = document.createElement('script');
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(script);

// grab the URLs
//var urls = $('.rg_di .rg_meta').map(function() { return JSON.parse($(this).text()).ou; });
var urls = $('.YQ4gaf').map(function() { return JSON.parse($(this).text()).ou; });

// write the URls to file (one per line)
var textToSave = urls.toArray().join('\n');
var hiddenElement = document.createElement('a');
hiddenElement.href = 'data:attachment/text,' + encodeURI(textToSave);
hiddenElement.target = '_blank';
hiddenElement.download = 'urls.txt';
hiddenElement.click();

///вот это заработало
var images = document.getElementsByClassName('ContentImage-Image ContentImage-Image_clickable');
var imageUrls = [];
for (var i = 0; i < images.length; i++) {
    if (!images[i].classList.contains('zr758c')) {
        imageUrls.push(images[i].src);
    }
}

var link = document.createElement('a');
link.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(imageUrls.join('\n')));
link.setAttribute('download', 'urls.txt');
link.style.display = 'none';
document.body.appendChild(link);
link.click();
document.body.removeChild(link);

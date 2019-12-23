// tslint:disable-next-line: no-var-requires
var fs = require('fs');
// tslint:disable-next-line: no-var-requires
var path = require('path');
var re = new RegExp('\\n第+[\u4e00-\u9fa5]+条+');
String.prototype.regexIndexOf = function (regex, startpos) {
    var indexOf = this.substring(startpos || 0).search(regex);
    return (indexOf >= 0) ? (indexOf + (startpos || 0)) : indexOf;
};
String.prototype.regexLastIndexOf = function (regex, startpos) {
    regex = (regex.global) ? regex :
        new RegExp(regex.source, 'g' + (regex.ignoreCase ? 'i' : '') + (regex.multiline ? 'm' : ''));
    if (typeof (startpos) === 'undefined') {
        startpos = this.length;
    }
    else if (startpos < 0) {
        startpos = 0;
    }
    var stringToWorkWith = this.substring(0, startpos + 1);
    var lastIndexOf = -1;
    var nextStop = 0;
    var result;
    // tslint:disable-next-line: no-conditional-assignment
    while ((result = regex.exec(stringToWorkWith)) != null) {
        lastIndexOf = result.index;
        regex.lastIndex = ++nextStop;
    }
    return lastIndexOf;
};
function search(keyWord) {
    // let ret = []
    var data = fs.readFileSync('./static/law/公安机关办理刑事案件程序规定.txt').toString();
    var pos = data.indexOf(keyWord);
    while (pos > -1) {
        var index1 = data.regexIndexOf(re, pos);
        var index2 = data.regexLastIndexOf(re, pos);
        // tslint:disable-next-line: no-console
        console.log(data.substring(index2, index1));
        // tslint:disable-next-line: no-console
        console.log('***********************************');
        data = data.substring(index1 + 1);
        pos = data.indexOf(keyWord);
    }
}
search('合法');

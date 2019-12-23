var fs = require('fs')
var path = require('path')

var re = new RegExp("\\n第+[\u4e00-\u9fa5]+条+")

String.prototype.regexIndexOf = function(regex, startpos) {
  var indexOf = this.substring(startpos || 0).search(regex);
  return (indexOf >= 0) ? (indexOf + (startpos || 0)) : indexOf;
}

String.prototype.regexLastIndexOf = function(regex, startpos) {
  regex = (regex.global) ? regex : new RegExp(regex.source, "g" + (regex.ignoreCase ? "i" : "") + (regex.multiline ? "m" : ""));
  if(typeof (startpos) == "undefined") {
      startpos = this.length;
  } else if(startpos < 0) {
      startpos = 0;
  }
  var stringToWorkWith = this.substring(0, startpos + 1);
  var lastIndexOf = -1;
  var nextStop = 0;
  let result;
  while((result = regex.exec(stringToWorkWith)) != null) {
      lastIndexOf = result.index;
      regex.lastIndex = ++nextStop;
  }
  return lastIndexOf;
}


function search(keyWord: string) {
  let ret = []
  let data = fs.readFileSync('./static/law/道路交通事故处理程序规定.txt').toString()
  let pos = data.indexOf(keyWord);
  if(pos > -1) {
    let index1 = data.regexIndexOf(re, pos)
    let index2 = data.regexLastIndexOf(re, pos)
    console.log(data.substring(index2, index1))
  }
}

search('列情形之一的')
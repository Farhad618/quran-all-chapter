let all = document.getElementsByClassName("quran-content")

let objs = Object.entries(all)

let txt = ""

for (var i = 2; i < objs.length; i++) {
	txt += objs[i][1].innerText + "\n"
}

console.log(txt)
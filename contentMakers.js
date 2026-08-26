function smp(text, imgSourceName, year="") {
  let yearDisplayed = year.length == 0 ? '' : `<p class="date">${year}</p>`;
    return `
    <section class="pageContent">
      <h1>
        ${text}
      </h1>
      <img src="./img/${imgSourceName}">
    </section>
    `
}


function simpleContentChapter( html, chapter ) {
let  chapterContent = [
"0: Why Europeans Crossed the Seas!",
"1: Colonization of India",
"2: Unequal Treaties and Exploitation",
"3: The British Raj",
"4: The Indian National Congress",
"5: The Non‑Violence Movement Arrives",
"6: The Shadow of Amritsar",
"7: The League Rises, Britain Trembles",
"8: India and Pakistan Emerge",
"9: India's Educational Transformation in Colonial Eras",
"10: The Cultural and Religious Soul of India",
"11: Arranged Marriages in India",
"12: The Beautiful Flora in India ",
"13: The Faunal Diversity in India ",
"14: The Many Faces of Indian Education",
];

let years = [

"",
"1505–1757",
"1757–1858",
"1858–1914",
"1885–1914",
"1915–1919",
"1919–1922",
"1922–1945",
"1945–1947",
"",
"",
"",
"",
"",
"",

];
let year = years[chapter];
  let yearDisplayed = year.length == 0 ? '' : `<p class="date">${year}</p>`;

    return `
    <section class="pageContent">
    <article class="chapterShower ch-${chapter}"> ${chapterContent[chapter]}</article>
        ${html}

      ${yearDisplayed}
    </section>
    `
}



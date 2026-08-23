function smp(text, imgSourceName, year="") {
  let yearDisplayed = year.length == 0 ? '' : `<p class="date">${year}</p>`;
    return `
    <section class="pageContent">
      <h1>
        ${text}
      </h1>
      <img src="./img/${imgSourceName}">
      ${yearDisplayed}
    </section>
    `
}



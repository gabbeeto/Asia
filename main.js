const previousButton = document.getElementById("previous");
const nextButton = document.getElementById("next");
let currentPage = 0
const lastPage = pageContainer.length;

function increaseCurrentPage() {
  const nextPage = currentPage + 1;
  if (nextPage == lastPage) {
    currentPage = 0;
  }
  else {
    currentPage = nextPage;

  }
}

function decreaseCurrentPage() {
  const previousPage = currentPage - 1;
  if (previousPage < 0) {
    currentPage = lastPage - 1;
  }
  else {
    currentPage = previousPage;

  }
}


const numberText = document.getElementById("number");
const contentContainer = document.getElementById("content")
function updateCount() {
  numberText.innerText = `${currentPage + 1}/${lastPage}`
  contentContainer.innerHTML = pageContainer[currentPage];
}

updateCount()

previousButton.addEventListener(
  "click", previousClick
)


nextButton.addEventListener(
  "click", nextClick
)

document.addEventListener("keydown", keyObj => {
  switch (keyObj.key) {
    case "ArrowRight":
    case "a":
    case "1":
    case "l":
      nextClick();
      break;
    case "ArrowLeft":
    case "s":
    case "2":
    case "h":
      previousClick();
      break;
  }
})

function previousClick() {
  decreaseCurrentPage()
  updateCount()
}


function nextClick() {
  increaseCurrentPage()
  updateCount()
}



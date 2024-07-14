let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");
let logoContainer = document.querySelector("#logo-container");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
  if (logoContainer.style.display === 'none') {
    logoContainer.style.display = 'block';
  } else {
    logoContainer.style.display = 'none';
  }
};

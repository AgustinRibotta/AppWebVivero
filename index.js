const nav = document.querySelector("#nav");
const openNav = document.querySelector("#open");
const close = document.querySelector("#close");

openNav.addEventListener("click", () => {
  nav.classList.add("visible");
});

close.addEventListener("click", () => {
  nav.classList.remove("visible");
});

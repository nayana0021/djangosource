// 하단의 페이지 나누기 영역 클릭 시
// href 값 가져오기
document.querySelector(".pagination").addEventListener("click", (e) => {
  // a 동작중지
  e.preventDefault();

  // href 가져오기
  let href = e.target.getAttribute("href");
  console.log(href);
});

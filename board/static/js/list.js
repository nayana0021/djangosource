// 하단의 페이지 나누기 영역 클릭 시
// href 값 가져오기
document.querySelector(".pagination").addEventListener("click", (e) => {
  // a 동작중지
  e.preventDefault();

  // href 가져오기
  let href = e.target.getAttribute("href");
  console.log(href);

  //href 값 actionForm 의 page value 값 대입
  document.querySelector("#page").value = href;
  // actionForm 전송
  document.querySelector("#actionForm").submit();
});

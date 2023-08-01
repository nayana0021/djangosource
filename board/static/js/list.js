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

// 검색
// 찾기 버튼 클릭 시 submit 막기
// 검색어 입력 여부 확인하기
// 검색어가 없으면 alert()
// 검색어가 있으면 하단의 actionForm 안 keyword value 값으로 삽입
// form submit()

document.querySelector("#btn-search").addEventListener("click", (e) => {
  e.preventDefault();

  const top_keyword = document.querySelector("#top_keyword");

  if (top_keyword.value == "") {
    alert("검색어를 입력하세요.");
    top_keyword.focus();
    return;
  }

  document.querySelector("#keyword").value = top_keyword.value;
  document.querySelector("#actionForm").submit();
});

// 정렬 기준 변화 시 값을 가져와서
// actionForm page=1로 변경
// actionForm에 sort 에 값 변경한 후 actionForm 전송
document.querySelector(".so").addEventListener("change", (e) => {
  const sort = e.target.value;
  document.querySelector("#page").value = 1;
  document.querySelector("#sort").value = sort;
  document.querySelector("#actionForm").submit();
});

// 제목 클릭 시
// a 태그 중지, href 값 가져오기
// actionForm 의 action 값을 가져온 href 변경 후 actionForm submit
const titles = document.querySelectorAll(".text-decoration-none");

titles.forEach((title) => {
  title.addEventListener("click", (e) => {
    e.preventDefault();

    let actionForm = document.querySelector("#actionForm");
    actionForm.action = e.target.href;
    actionForm.submit();
  });
});

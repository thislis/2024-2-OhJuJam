<script>
  import { onMount } from 'svelte';

  const request_post = async (endpoint, data) => {
      const resp = await fetch(`http://localhost:8000${endpoint}`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
      });
      return resp;
  };

  const request_get = async () => {
      const resp = await fetch(`http://localhost:8000/door/load`);
      if (!resp.ok) { // 응답이 성공적이지 않을 경우 오류 처리
          throw new Error(`HTTP error! status: ${resp.status}`);
      }
      const result = await resp.text();
      return result;
  };
  
  let choice = 0;

  const click = () => {
      choice += 1;
  };

  const post_action = (event) => {
      event.preventDefault();
      const get_radio = document.getElementsByName('product');
      let your_action;
      get_radio.forEach((radio) => {
          if (radio.checked) {
              your_action = parseInt(radio.value); // 정수형으로 변환
          }
      });

      if (your_action !== undefined) {
          // 'name'과 'win'을 포함한 데이터 전송
          request_post('/door/open', { your_action, name, win }).then(response => {
              console.log("Response from server:", response.message);
          }).catch(error => {
              console.error("Error:", error);
          });
      } else {
          console.log("No action selected.");
      }
  };

  let state = "";
  let win = 0;

  const get_door_state = async () => {
      try {
          state = await request_get(); // 서버에서 상태를 가져옴
          console.log("Door state:", state); // 상태를 콘솔에 출력

          if ((choice % 2 === 1 && state === "Opened") || (choice % 2 === 0 && state === "Reverse Opened")) {
            win = win + 1
          }

      } catch (error) {
          console.error("Error fetching door state:", error); // 오류 발생 시 로그
      }
  };

  let name = "";

  const update_ranking = async (name, win) => {
    if (name) {
        request_post('/ranking/update', { name, win }).then(response => {
            console.log("Response from server:", response.message);
        }).catch(error => {
            console.error("Error:", error);
        });
    } else {
        console.log("No NAME?");
    }
  };

  let rankings = [];
  let showRankings = false;

  const fetchRankings = async () => {
    const response = await fetch('http://localhost:8000/ranking/load');
    if (response.ok) {
      const data = await response.json();
      rankings = Object.values(data).map((rank, index) => ({
        rank: index + 1,
        name: rank.name,
        win: rank.win
      }));
    }
  };

  const toggleRankings = () => {
    if (showRankings) {
      rankings = [];
    } else {
      fetchRankings();
    }
    showRankings = !showRankings;
  };
</script>

<main>
  <h1>OPEN? or Reverse OPEN?</h1>

  <div class="card">
      <button onclick={click}>
          {#if choice % 2 == 0}
              your choice is Reverse Opened
          {:else}
              your choice is Opened
          {/if}
      </button>
  </div>

  <form class="product_container" onsubmit={post_action}>
      <input type="radio" name="product" id="product_a" value="1" />
      <label for="product_a">
          <p>OPEN</p>
          <span>Open the door</span>
      </label>

      <input type="radio" name="product" id="product_b" value="0" />
      <label for="product_b">
          <p>No OPEN</p>
          <span>No action</span>
      </label>
      <input type="radio" name="product" id="product_c" value="2" />
      <label for="product_c">
          <p>Reverse OPEN</p>
          <span>Reverse open the door</span>
      </label>

      <button type="submit">Submit</button>
  </form>

  <p class="read-the-docs">
      Click on the button, And choose that door is opened or reverse opened!<br/>
      Choose your action, check if your choice is right!
  </p>

  <button onclick={() => get_door_state()}>Is Door Opened?</button>
  <p>{state}<br/>win: {win}</p>

  <input bind:value={name}>
  <button onclick={() => update_ranking(name)}>rank your winning!</button>

</main>

<button onclick={toggleRankings}>
  {showRankings ? '순위표 숨기기' : '순위표 보기'}
</button>

{#if showRankings}
  <div class="rankings">
    <h2>순위표</h2>
    <table>
      <thead>
        <tr>
          <th>순위</th>
          <th>이름</th>
          <th>승수</th>
        </tr>
      </thead>
      <tbody>
        {#each rankings as ranking}
          <tr>
            <td>{ranking.rank}</td>
            <td>{ranking.name}</td>
            <td>{ranking.win}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{/if}

<style>
  input[name="product"] {
      display: none;
  }

  .product_container {
      display: flex;
      flex-direction: row;
      width: cal(100% - 500px);
      margin: 0px auto;
      gap: 30px;
  }

  .read-the-docs {
      color: rgb(154, 154, 154);
  }

  form {
      font-family: "Pretendard";
  }
  form label {
      display: flex;
      flex-direction: column;
      gap: 10px;
      border: 1px solid #e1e1e1;
      border-radius: 13px;
      width: 100%;
      justify-content: center;

      padding: 30px 5px;
      box-sizing: border-box;
      cursor: pointer;
      transition: background-color 0.3s;
  }
  form label p {
      font-weight: 700;
      font-size: 18px;
      margin: 0px;
  }

  /* 체크 시 버튼 모양 스타일*/
  input[name="product"]:checked + label {
      background-color: #000066;
  }

  .rankings {
    margin: 20px 0;
    border: 1px solid #ccc;
    padding: 10px;
  }
</style>

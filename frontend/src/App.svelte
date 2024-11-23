<script>
  import { onMount } from 'svelte';

  const request_post = async (endpoint, data) => {
      const resp = await fetch(`https://gamja.hexa.pro${endpoint}`, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
      });
      return resp;
  };

  const request_get = async () => {
      const resp = await fetch(`https://gamja.hexa.pro/door/load`);
      if (!resp.ok) {
          throw new Error(`HTTP error! status: ${resp.status}`);
      }
      const result = await resp.text();
      return result;
  };

  let choice = 0;
  let name = "";
  let state = "";
  let showState = false; // 상태를 보여줄지 여부를 관리하는 변수

  const click = () => {
      choice += 1;
  };

  const post_action = async (event) => {
      event.preventDefault();
      const get_radio = document.getElementsByName('product');
      let your_action;
      get_radio.forEach((radio) => {
          if (radio.checked) {
              your_action = parseInt(radio.value);
          }
      });

      if (your_action !== undefined) {
          await request_post('/door/open', { your_action, name});
          // 상태를 업데이트하지 않음
      } else {
          console.log("No action selected.");
      }
  };

  const get_door_state = async () => {
      try {
          state = await request_get(); // 서버에서 상태를 가져옴
          console.log("Door state:", state); // 상태를 콘솔에 출력

          showState = true; // 버튼 클릭 시 상태를 보여줌

      } catch (error) {
          console.error("Error fetching door state:", error);
      }
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
  <br/>
  
  <button onclick={() => get_door_state()}>Is Door Opened?</button><br/>
  {#if showState} <!-- 상태가 보여야 할 때만 표시 -->
  <p>{state}</p>
{/if}

</main>

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
</style>

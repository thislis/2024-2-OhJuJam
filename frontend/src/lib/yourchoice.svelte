<script>
    let choice = $state(0);
    let room_num;
    let your_action;

    const click = () => {
        choice += 1;
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

    <form class="product_container">
        <input type="radio" name="product" id="product_a" value="A" />
        <label for="product_a">
            <p>OPEN</p>
            <span>Open the door</span>
        </label>

        <input type="radio" name="product" id="product_b" value="B" />
        <label for="product_b">
            <p>No OPEN</p>
            <span>No action</span>
        </label>
        <input type="radio" name="product" id="product_c" value="C" />
        <label for="product_c">
            <p>Reverse OPEN</p>
            <span>Reverse open the door</span>
        </label>
    </form>

    <p class="read-the-docs">
        Click on the button, And choose that door is opened or reverse opened!<br
        />
        Choose your action, check if your choice is right!
    </p>
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
        background-color: red;
    }
</style>

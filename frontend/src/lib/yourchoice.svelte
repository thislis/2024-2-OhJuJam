<script>
    let choice = $state(0)

    const click = () => {
        choice += 1
    }

    const door_update = async (door_num) => {
        const is_door_opened = await fetch(`${door_num}`)
    }
</script>

<main>
    <h1>OPEN? or Reverse OPEN?</h1>
  
    <div class="card">
        <button onclick={click}>
            {#if choice%2 == 0}
                your choice is Closed
            {:else}
                your choice is Opened
            {/if}
        </button>
    </div>

    
  
    <p class="read-the-docs">
      Click on the button, And choose that door is opened or closed!
    </p>
  </main>
  
  <style>
    .read-the-docs {
      color: rgb(154, 154, 154);
    }
  </style>
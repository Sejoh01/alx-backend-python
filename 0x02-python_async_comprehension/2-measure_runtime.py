#!/usr/bin/env python3
import asyncio

async def measure_runtime(async_comprehension):
    """Measures the total runtime of executing async_comprehension four times in parallel."""

    start_time = time.time()  # Capture start time

    async def run_async_comprehension():
        await async_comprehension  # Execute the coroutine

    tasks = [asyncio.create_task(run_async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)  # Wait for all tasks to finish

    end_time = time.time()  # Capture end time
    total_runtime = end_time - start_time

    return total_runtime

# Assuming async_comprehension is defined in the previous file

async def main():
    runtime = await measure_runtime(async_comprehension)
    print(f"Total runtime of executing async_comprehension four times in parallel: {runtime:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())

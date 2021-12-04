// NOTE: Using Deno (v1.16.3), not Node

try {
	let numIncreased = 0
	const inputText = await Deno.readTextFile('input.txt')
	let prev: number | undefined
	inputText.split('\n').forEach(line => {
		let val = parseInt(line)
		if (!prev) {
			prev = val
			return
		}
		if (val > prev) {
			numIncreased++
		}
		prev = val
	})
	console.log(`Number of increases: ${numIncreased}`)
} catch (error) {
	console.error(error)
}


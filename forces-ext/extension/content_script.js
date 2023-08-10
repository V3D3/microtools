function getcontest ()
{
	// match url
	// customization: add more url matchers
	let url = window.location.href;
	let p1  = /codeforces.com\/problemset\/problem\/([0-9]+)/;
	let p2 = /codeforces.com\/contest\/([0-9]+)/;

	if (url.match (p1))
		return url.match (p1)[1];
	if (url.match (p2))
		return url.match (p2)[1];
}

function getproblem ()
{
	// customization: add more problem matchers
	let url = window.location.href;
	let p1 = /codeforces.com\/problemset\/problem\/[0-9]+\/([A-Z][0-9]?)/;
	let p2 = /codeforces.com\/contest\/[0-9]*\/problem\/([A-Z][0-9]?)/;

	if (url.match (p1))
		return url.match (p1)[1];
	if (url.match (p2))
		return url.match (p2)[1];
}

function purify (casestr)
{
	// customization: add more regexes (in case of varying test case box format)
	let p1 = "input\nCopy\n"
	let p2 = "output\nCopy\n"

	if (casestr.indexOf (p1) == 0)
		return casestr.split (p1)[1];
	if (casestr.indexOf (p2) == 0)
		return casestr.split (p2)[1];
}

function gettests ()
{
	// customization: change scraping method
	let inps = document.getElementsByClassName ('input');
	let outs = document.getElementsByClassName ('output');

	let res = [];

	for (let i = 0; i < inps.length; i++)
	{
		let obj = {};
		obj['i'] = purify (inps[i].innerText);
		obj['o'] = purify (outs[i].innerText);

		res.push (obj)
	}

	return res;
}

function openreq ()
{
	// customization: change endpoint based on url, to add more site support
	let contest = getcontest ();
	let problem = getproblem ();
	let tests = gettests ();

	fetch ("http://localhost:20000/problem/" + contest + "/" + problem, {method: "POST",headers: {"Content-Type": "application/json"}, body: JSON.stringify ({"cases": tests})});
}

// customization: trigger from keystroke, or button, or on page load, etc
let button = document.createElement ('button');
button.innerHTML = "Load";

document.body.appendChild (button);

button.addEventListener(
    "click", () => openreq (), false);

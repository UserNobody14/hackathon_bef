// ==UserScript==
// @name         Hackerscript
// @namespace    http://tampermonkey.net/
// @version      2024-03-23
// @description  try to take over the world!
// @author       You
// @match        https://www.google.com/
// @match        https://vanjs.org/*
// @match      *://*/**
// @icon         https://www.google.com/s2/favicons?sz=64&domain=google.com
// @grant GM_setValue
// @grant GM_getValue
// @grant GM.setValue
// @grant GM.getValue
// @grant GM_setClipboard
// @grant unsafeWindow
// @grant window.close
// @grant window.focus
// @grant window.onurlchange
// @grant GM_xmlhttpRequest
// @require      https://cdn.jsdelivr.net/gh/vanjs-org/van/public/van-1.5.0.nomodule.min.js
// ==/UserScript==
(function() {
    'use strict';

    function setInputValues(inputData, forms) {

        if (typeof inputData === "string") {
            console.log("DJnflsjhdflhjs");
            inputData = JSON.parse(inputData);
        }
        console.log(typeof inputData, inputData);

        // Iterate over each form
        forms.forEach((form, index) => {
            console.log("FRM", form);


            // Ensure there's corresponding input data for the form
            if (index < inputData.length) {
                const data = inputData[index];
                console.log("DATA",data, index, inputData);
                // Iterate over each key in the data object
                for (const key in data) {
                    // Find the input element with the name equal to the current key
                    const input = form.querySelector(`input[name="${key}"],textarea[name="${key}"]`);

                    // If the input exists, set its value
                    if (input) {
                        input.value = data[key];
                    }
                }
            }
        });
    }

    async function getFromValues(values, promptValue) {

        GM_xmlhttpRequest();

        const ffv = await GM.xmlHttpRequest(
            {
                method: "POST",
                url: "http://localhost:8000/forms",
                responseType: 'json',
                headers: {
                    "Content-Type": "application/json"
                },
                onload: function(response) {
                    console.log(response.responseText);
                },
                data: JSON.stringify({
                    forms: values,
                    prompt: promptValue
                }),

            }
        ).catch(e => console.error(e));
        console.log(ffv.responseText);


        /*const ffv = await fetch(
        "http://localhost:8000/forms",
            {
            method: "POST",
            headers: {
            'Content-Type': "application/json",
            },
            body: JSON.stringify({
                forms: values
            }),
        url: "http://127.0.0.1:8000/forms",
        });*/
        console.log("CHECKINJN",ffv);
        const jj = JSON.parse(ffv.responseText);
        console.log("JSONNIC",jj, ffv)
        return jj;
        // Dummy fn
        /**
        return Promise.resolve([{
            ei: "TEST1",
            q: "CHECKTEST",

        }])
*/
    }

    var formValues = null;

    console.log("VAN",van);

    const {button, div, pre, textarea, input} = van.tags

    const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

    const Run = ({sleepMs}) => {
        const steps = van.state(0)
        ;(async () => { for (; steps.val < 40; ++steps.val) await sleep(sleepMs) })()
        return pre(() => `${" ".repeat(40 - steps.val)}🚐💨Hello VanJS!${"_".repeat(steps.val)}`)
    }

    const Hello = () => {
        const prompt = van.state('');
        const loading = van.state(false);
        const error = van.state(false);
        const divstyle = van.derive(
        () => `
                position: absolute;
                bottom: 0;
                left: 0;
                font-size: 64px;
                height: 30vh;
                width: 40vw;
                min-width: 30rem;
                min-height: 20rem;
                max-height: 500px;
                max-width: 500px;
                z-index: 2900;
                background-color: ${error.val ? 'red' : 'transparent'};
                padding: 2rem;
                `
        );
        const dom = div()
        return div(
            dom,
            div({
                class: 'MY_HACKED_CLASS',
                style: divstyle,
            },
                textarea({
                name: 'prompt',
                value: prompt,
                onchange: (e) => {
                    console.log("VAN", prompt.val);
                    prompt.val = e.target.value;
                },
                onkeydown: (e) => {
                    console.log(e);
                    if (e.key === "Enter") {
                        // TODO: signal backend
                        console.log("BACKEND SIGNALLED");
                        const backValue = document.querySelectorAll('form');
                        console.log("ALL BACKEND FORMS?", backValue);
                        formValues = backValue;
                        const htmlList = Array.from(formValues).map(node => node.outerHTML);
                        console.log("Sent to the backend", htmlList);
                        loading.val = true;
                        getFromValues(htmlList, prompt.val).then(vv => {
                            console.log("RESULTS RECEIRVED", vv);
                            setInputValues(vv, backValue);
                            loading.val = false;
                        }).catch((ee) => {
                            error.val = ee;
                            loading.val = false;
                        });


                    }
                },
                disabled: loading,

                style: `
                                font-size: 1.5rem;

                width: 90%;
                height: 90%;
                max-width: 100%;
                max-height: 100%;

                `
            })
               )
        )
    }

    van.add(document.body, Hello())

})();
import axios from "axios";
import useSWR from "swr";

function createRequest() {
    return axios.create()
}

export function useGetter(url, config) {
    const request = createRequest()
    return useSWR(url, async (url) => await request.get(url, config).then(res => res.data).catch(err => err.response || err))
}

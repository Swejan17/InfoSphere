import { Box } from "@mui/material"
import "github-markdown-css/github-markdown-light.css"
import { useParams } from "react-router-dom"
import { useGetter } from "./hooks/fetcher"

export default function Content() {
    const { id } = useParams()
    const { data: content } = useGetter("http://localhost:6969/api/findById/"+id)
    return (
        <Box className="markdown-body" padding={"6rem"}>
            <h1>{content?.title.trim()}</h1>
            {content?.content?.trim().split("\n")?.map(e => <p>{e?.trim()}</p>)}
        </Box>
    )
}
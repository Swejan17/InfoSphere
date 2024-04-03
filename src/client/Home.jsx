import ClearIcon from '@mui/icons-material/Clear';
import SearchIcon from '@mui/icons-material/Search';
import {
    Button,
    InputAdornment,
    Paper,
    Stack,
    TextField,
    Typography
} from "@mui/material";
import { DataGrid } from '@mui/x-data-grid';
import axios from "axios";
import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

export default function Home() {
    const { q } = useParams()
    const navigate = useNavigate()
    const columns = [
        {
            field: 'id',
            headerName: 'ID',
            width: 90
        },
        {
            field: 'title',
            headerName: 'Title',
            width: 600,
        }
    ]
    const [searchText, setSearchText] = useState(q)
    const [results, setResults] = useState([])
    const [time, setTime] = useState(-1)
    const handleSubmit = async () => {
        const res = await axios.get("http://localhost:6969/api/search?q=" + searchText).then(res => res.data)
        if (res) {
            setSearchText("")
            setResults(res?.data)
            setTime(res?.time)
        }
    }
    return (
        <Stack
            direction={"column"}
            gap={"2rem"}
            justifyContent={"space-evenly"}
            alignItems={"center"}
            padding={"2rem"}
        >
            <Paper
                sx={{
                    width: "40%",
                    padding: ".75rem",
                    display: "flex",
                    justifyContent: "space-between",
                    alignItems: "center",
                    gap: "1.25rem"
                }}
            >
                <Stack direction={"row"} justifyContent={"center"} alignItems={"center"} gap={"5px"}>
                    <img src="/logo.png" alt="Logo" height={40} width={40} />
                    <Typography variant="h5" component="div">InfoSphere</Typography>
                </Stack>
                <TextField
                    value={searchText}
                    onChange={(e) => setSearchText(e.target.value)}
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <SearchIcon />
                            </InputAdornment>
                        ),
                        ...(searchText && {
                            endAdornment: (
                                <InputAdornment
                                    position="end"
                                    onClick={() => setSearchText("")}
                                    sx={{
                                        ":hover": {
                                            cursor: "pointer"
                                        }
                                    }}
                                >
                                    <ClearIcon />
                                </InputAdornment>
                            )
                        })
                    }}
                    fullWidth
                    variant="standard"
                />
                <Button variant="contained" onClick={handleSubmit}>
                    Search
                </Button>
            </Paper>
            <Stack direction={"column"} justifyContent={"center"}>
                {results.length>0 ? (
                    <Stack direction={"column"} justifyContent={"center"} alignItems={"end"} gap={"1px"}>
                        <DataGrid
                            rows={results}
                            columns={columns}
                            initialState={{
                                pagination: {
                                    paginationModel: {
                                        pageSize: 10,
                                    },
                                },
                            }}
                            pageSizeOptions={[10]}
                            disableRowSelectionOnClick
                            sx={{
                                width: 750
                            }}
                            onRowClick={(params) => {
                                navigate("/content/"+params.id)
                            }}
                        />
                        <Typography variant="body2">Searched {results?.length} of 467000 results in {time} sec</Typography>
                    </Stack>
                ): (
                    <Typography variant="body2">Nothing to search</Typography>
                )}
            </Stack>
        </Stack>
    );
}
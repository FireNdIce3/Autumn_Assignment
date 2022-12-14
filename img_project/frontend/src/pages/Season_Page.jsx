import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  fetchRounds,
  roundsChanged,
  roundsVisibilityChanged,
  selectedSeasonIdChanged,
} from "../app/features/drawerSlice";
import axios from "axios";
import { useParams } from "react-router-dom";
import { Typography } from "@mui/material";


const style = {
  width: `100%`,
  paddingTop: `50px`,
}

export default function Season(props) {
  const { id } = useParams();
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(selectedRoundChanged(null));
    dispatch(roundsVisibilityChanged(true));
    dispatch(selectedSeasonIdChanged(id));
    dispatch(fetchRounds())
  }, []);

  useEffect(() => {
    axios({
      method: "get",
      url: `http://localhost:8000/api/seasons/${id}`,
      headers: {
        Authorization: "Token " + localStorage.getItem("token"),
      },
    }).then((response) => {
      dispatch(titleChanged(response.data.name));
    });
  }, [id]);

  return (
    <div style={style}>
    </div>
  );
}

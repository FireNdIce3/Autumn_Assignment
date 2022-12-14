import * as React from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import Typography from "@mui/material/Typography";
import { Box, Skeleton } from "@mui/material";
import { makeStyles } from "@mui/styles";
import { useSelector, useDispatch } from "react-redux";
import { fetchRounds, toggled } from "../app/features/drawerSlice";
import { List, ListItem, ListItemButton, ListItemText } from "@mui/material";
import { selectedRoundChanged } from "../app/features/seasonSlice";
import { Button } from "@mui/material";
import { Modal } from "@mui/material";
import { TextField } from "@mui/material";
import { MenuItem } from "@mui/material";
import axios from "axios";
import { toast, ToastContainer } from "react-toastify";
import { Link, useNavigate } from "react-router-dom";
import "react-toastify/dist/ReactToastify.css";
import { useState, useEffect } from "react";
import { InfoRounded } from "@mui/icons-material";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "1px solid #000",
  boxShadow: 24,
  p: 4,
  borderRadius: `10px`,
};

const colorTypographyStyle = {
  background: `linear-gradient(to right, rgba(218,111,158,1) 0%, rgba(25,118,210,1) 100%)`,
  WebkitBackgroundClip: "text",
  WebkitTextFillColor: `transparent`,
};

const useStyles = makeStyles((theme) => ({
  appBar: {
    position: "absolute",
  },
  addRoundBtnContainer: {
    position: `absolute`,
    bottom: `20px`,
    width: `100%`,
    display: `flex`,
    justifyContent: `center`,
  },
  inputRoundName: {
    width: `100%`,
    marginTop: `10px !important`,
  },
  inputRoundType: {
    width: `100%`,
    marginTop: `10px !important`,
  },
  createRoundBtnContainer: {
    display: `flex`,
    justifyContent: `flex-end`,
    marginTop: `15px`,
  },
  profileDetailsContainer: {
    display: `flex`,
    flexDirection: `column`,
    gap: `10px`,
    alignItems: `center`,
    paddingTop: `30px`,
    wordWrap: `break-word`,
    whiteSpace: `normal`,
  },
}));

const drawerWidth = 270;

function AppDrawer(props) {
  const { window } = props;
  const dispatch = useDispatch();
  const isDrawerVisible = useSelector((state) => state.drawer.drawerVisible);
  const isLoading = useSelector((state) => state.drawer.loading);
  const [open, setOpen] = React.useState(false);
  const [option, setOption] = React.useState("T");
  const navigate = useNavigate();
  const [currentUser, setCurrentUser] = useState(null);

  const showRoundSuccessToast = () => {
    toast.success("Round Created", {
      position: "bottom-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "light",
    });
  };

  const classes = useStyles();
  const {
    appBar,
    addRoundBtnContainer,
    inputRoundName,
    inputRoundType,
    createRoundBtnContainer,
    profileDetailsContainer,
  } = classes;

  const isRoundsListVisible = useSelector(
    (state) => state.drawer.roundsVisible
  );

  const handleChange = (event) => {
    setOption(event.target.value);
  };

  const selectedSeasonId = useSelector(
    (state) => state.drawer.selectedSeasonId
  );

  const selectedRound = useSelector((state) => state.season.selectedRound);

  const handleRoundChange = (round) => {
    round.round_type === "T"
      ? navigate(`/season/${selectedSeasonId}/test/${round.id}`)
      : navigate(`/season/${selectedSeasonId}/interview/${round.id}`);
    dispatch(selectedRoundChanged(round.id));
  };

  const handleCreateRound = () => {
    const roundName = document.getElementById("input-round-name").value;
    axios({
      method: "post",
      url: `http://localhost:8000/api/roundDetails/`,
      headers: {
        Authorization: "Token " + localStorage.getItem("token"),
      },
      data: {
        round_name: roundName,
        round_type: option,
        season: selectedSeasonId,
      },
    }).then((response) => {
      showRoundSuccessToast();
      setOpen(false);
      dispatch(fetchRounds());
    });
  };

  const rounds = useSelector((state) => state.drawer.rounds);

  const roundsList = (
    <List>
      {rounds.length ? (
        <>
          {rounds.map((round) => (
            <ListItem disablePadding key={round.id}>
              <ListItemButton
                onClick={() => handleRoundChange(round)}
                style={{
                  textAlign: `center`,
                }}
              >
                <ListItemText
                  disableTypography
                  primary={
                    <Typography
                      sx={
                        selectedRound &&
                        selectedRound === round.id &&
                        colorTypographyStyle
                      }
                    >
                      {round.round_name.length > 25
                        ? round.round_name.substr(0, 25) + "..."
                        : round.round_name}
                    </Typography>
                  }
                />
              </ListItemButton>
            </ListItem>
          ))}
        </>
      ) : isLoading ? (
        <>
          <Skeleton animation="wave" width={"80px"} />
          <Skeleton animation="wave" />
          <Skeleton animation="wave" />
        </>
      ) : (
        <Typography align="center">Nothing here.</Typography>
      )}
    </List>
  );

  const addRoundBtn = (
    <div className={addRoundBtnContainer}>
      <Button variant="contained" onClick={() => setOpen(true)} sx={{}}>
        + Add Round
      </Button>
    </div>
  );

  const drawer = (
    <div>
      <Box
        sx={{
          p: 2,
          height: `65px`,
          width: `100%`,
          textAlign: "center",
        }}
      >
        <Link
          to="/seasons/"
          style={{
            textDecoration: `none`,
            color: `black`,
          }}
        >
          <Typography variant="h6" sx={colorTypographyStyle}>
            IMG Recruitments
          </Typography>
        </Link>
      </Box>
      <Divider />
      {isRoundsListVisible
        ? roundsList
        : currentUser && (
            <div className={profileDetailsContainer}>
              <Typography
                variant="h5"
                sx={{
                  marginBottom: `20px`,
                  background: `linear-gradient(to right, rgba(218,111,158,1) 0%, rgba(25,118,210,1) 100%)`,
                  WebkitBackgroundClip: "text",
                  WebkitTextFillColor: `transparent`,
                }}
              >
                <InfoRounded
                  sx={{
                    marginTop: `-3px`,
                    marginRight: `3px`,
                    color: `#c270a4`,
                  }}
                />
                <b>Your Info</b>
              </Typography>
              <img
                src={currentUser.image}
                style={{
                  width: `140px`,
                  height: `auto`,
                  borderRadius: `50%`,
                }}
              />
              <Typography
                variant="h6"
                sx={{
                  textAlign: `center`,
                }}
              >
                <b>{currentUser.name}</b>
              </Typography>
              <Typography variant="subtitle1">
                {currentUser.enrolment_number}
              </Typography>
              <Typography
                variant="subtitle1"
                sx={{
                  textAlign: `center`,
                }}
              >
                {currentUser.branch}
              </Typography>
              <Typography
                variant="subtitle1"
                sx={{
                  textAlign: `center`,
                }}
              >
                {currentUser.year} Year
              </Typography>

              <Typography
                variant="subtitle1"
                sx={{
                  textAlign: `center`,
                }}
              >
                {currentUser.email}
              </Typography>
            </div>
          )}
      {isRoundsListVisible ? addRoundBtn : <></>}
    </div>
  );

  const container =
    window !== undefined ? () => window().document.body : undefined;

  const roundTypes = [
    {
      label: "Test",
      value: "T",
    },
    {
      label: "Interview",
      value: "I",
    },
  ];

  useEffect(() => {
    if (localStorage.getItem("token")) {
      axios({
        method: "get",
        url: `http://localhost:8000/api/current_user/`,
        headers: {
          Authorization: "Token " + localStorage.getItem("token"),
        },
      })
        .then((response) => {
          setCurrentUser(response.data[0]);
        })
        .catch((response) => {
          console.log(response.message);
        });
    }
  }, []);

  return (
    <>
      <CssBaseline />
      <Drawer
        container={container}
        variant="temporary"
        open={isDrawerVisible}
        onClose={() => dispatch(toggled())}
        ModalProps={{
          keepMounted: true, // Better open performance on mobile.
        }}
        sx={{
          display: { xs: "block", sm: "none" },
          "& .MuiDrawer-paper": { width: drawerWidth },
        }}
      >
        {drawer}
      </Drawer>
      <Drawer
        variant="permanent"
        sx={{
          whiteSpace: "nowrap",
          display: { xs: "none", sm: "block" },
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            position: "relative",
            height: `100vh`,
          },
        }}
        anchor="left"
      >
        {drawer}
      </Drawer>
      <Modal
        open={open}
        onClose={() => setOpen(false)}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="h6" component="h2">
            Adding Round
          </Typography>
          <TextField
            id="input-round-name"
            label="Round Name"
            variant="filled"
            className={inputRoundName}
          />
          <TextField
            id="input-round-type"
            select
            label="Select Round Type"
            value={option}
            onChange={handleChange}
            helperText="Please select the round type."
            variant="filled"
            className={inputRoundType}
          >
            {roundTypes.map((roundType) => (
              <MenuItem key={roundType.value} value={roundType.value}>
                {roundType.label}
              </MenuItem>
            ))}
          </TextField>
          <div className={createRoundBtnContainer}>
            <Button variant="contained" onClick={handleCreateRound}>
              Create
            </Button>
          </div>
        </Box>
      </Modal>
      <ToastContainer
        position="bottom-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
      />
    </>
  );
}

export default AppDrawer;

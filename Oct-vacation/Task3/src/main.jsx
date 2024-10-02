import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import {
  FluentProvider,
  webLightTheme,
  webDarkTheme,
} from "@fluentui/react-components"
import './main.css'
import App from "./App.jsx"

const getSystemTheme = () =>
  window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
    ? webDarkTheme
    : webLightTheme

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <FluentProvider theme={getSystemTheme()} className="root">
      <App />
    </FluentProvider>
  </StrictMode>
)

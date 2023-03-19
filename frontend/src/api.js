import axios from 'axios';

import { API } from '@/settings.js'

export const PingGet = async () => {
  const url = `${API}/ping/`;

  return await axios.get(url);
};

export const PingPost = async () => {
  const url = `${API}/ping/`;

  return await axios.post(url, {
    random_data: "123"
  });
};

export const Wrong = async () => {
  const url = `${API}/not_existing_address_for_tests`;

  return await axios.get(url);
};

export const GetKeys = async () => {
  const url = `${API}/task/keys`;

  return await axios.get(url);
};

export const Install = async (input_data) => {
  const url = `${API}/task/`;

  return await axios.post(url, input_data);
};


export const Status = async task_id => {
  const url = `${API}/task/${task_id}`;

  return await axios.get(url);
};

export const Configs = async (task_id, data_key) => {
  const url = `${API}/task/${task_id}/configs?data_key=${data_key}`;

  return await axios.get(url);
};

export const Stdout = async task_id => {
  const url = `${API}/task/${task_id}/stdout`;

  return await axios.get(url);
};

export const STATUS_STATES = {
  pending: "PENDING",
  started: "STARTED",
  progress: "PROGRESS",
  success: "SUCCESS",
  failure: "FAILURE"
}
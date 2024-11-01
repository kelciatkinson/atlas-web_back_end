export default function loadBalancer(chinaDownload, USDownload) {
  return new Promise((resolve) => {
    const balancer = Math.random() < 0.5;
    if (balancer) {
      resolve({ load: chinaDownload });
    } else {
      resolve({ load: USDownload });
    }
  });
}

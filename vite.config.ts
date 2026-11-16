import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
export default defineConfig({plugins:[react()],base:'./',build:{sourcemap:false,rollupOptions:{output:{manualChunks(id){if(id.includes('node_modules'))return 'vendor';if(id.includes('/src/data/'))return 'content';}}}},server:{port:5173,strictPort:true,watch:{ignored:['**/.tools/**','**/.pnpm-store/**','**/private/**','**/releases/**']}}});
